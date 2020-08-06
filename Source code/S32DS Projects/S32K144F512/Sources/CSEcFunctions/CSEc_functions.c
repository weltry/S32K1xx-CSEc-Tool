#include "CSEc_functions.h"
#include "CSEC1.h"

static const uint8_t KEY_UPDATE_ENC_C[16] = {0x01u,0x01u,0x53u,0x48u,0x45u,0x00u,0x80u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0xB0u};
static const uint8_t KEY_UPDATE_MAC_C[16] = {0x01u,0x02u,0x53u,0x48u,0x45u,0x00u,0x80u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0xB0u};
static const uint8_t DEBUG_KEY_C[16]      = {0x01u,0x03u,0x53u,0x48u,0x45u,0x00u,0x80u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0xB0u};

static uint8_t  KDF(const uint8_t *authorizing_key,const uint8_t *constant,uint8_t *K_out);


/*FUNCTION**********************************************************************
 *
 * Function Name : KDF
 * Description   :
 * Implements    :
 * END**************************************************************************/
static uint8_t KDF(const uint8_t *AuthKey, const uint8_t *Constant,uint8_t *K_out)
{
    uint8_t Res,i,Concat[32u];
    for (i = 0u; i < 16u; i++)
    {
        Concat[i]	 = AuthKey[i];
        Concat[i+16] = Constant[i];
    }
	Res = CSEC_DRV_MPCompress(Concat, 2u, K_out, 2u);
    return Res;
}


/*FUNCTION**********************************************************************
 *
 * Function Name : CalculateM1ToM5
 * Description   : calculate M1 to M5
 * Using UID=0, please get the real UID by yourself if it necessary
 * Implements    :
 * END**************************************************************************/
uint16_t CalculateM1ToM5(uint8_t *authorizing_key, uint8_t *new_key, uint8_t auth_key_id, uint8_t key_id, uint32_t counter, uint8_t attribute_flags,
						          uint8_t *M1_out, uint8_t *M2_out, uint8_t *M3_out, uint8_t *M4_out, uint8_t *M5_out)
{
	uint8_t UID[16u]     = {0u};
	uint8_t UID_MAC[16u] = {0u};
	uint8_t M4_star[16u] = {0u};
	uint8_t M4_tmp[16u]  = {0u};
	uint8_t K_out[16u]   = {0u};
	uint8_t Iv[16u]      = {0u};
	uint8_t PLAIN_TEXT[32u] = {0u};
	uint8_t M1M2[48u]     = {0u};
	uint8_t Challenge[16u]  = {0u, 1u, 2u, 3u, 4u, 5u, 6u, 7u, 8u, 9u, 10u, 11u, 12u, 13u, 14u, 15u};
	uint8_t Sreg=0u;
	uint8_t i = 0u;
	uint16_t Res=0u;


    //For keys in the other bank, don't consider the KBS bit in M1 & M4 calculation. Follow traditional SHE specs
    //****Calculate M1****
	if(attribute_flags & 0x08)
	{
		Res |= CSEC_DRV_GetID(Challenge,UID,&Sreg,UID_MAC);
	}
    for(i=0u;i<15u;i++)
    {
		M1_out[i] = UID[i];
	}
	M1_out[15u] = ((key_id & 0x0Fu)<<4u) | (auth_key_id & 0x0Fu);

	//****Calculate M2****
	//First, calculate K1 and load K1 into RAM
	Res |= KDF(authorizing_key, KEY_UPDATE_ENC_C,K_out);
	Res |= CSEC_DRV_LoadPlainKey(K_out);
	//Second, concatenate the input data
	//0bit~27bit:CID  28bit~32bit:FID
	PLAIN_TEXT[0u] = (uint8_t)((counter &  0x0FF00000u) >> 20u);
	PLAIN_TEXT[1u] = (uint8_t)((counter &  0x000FF000u) >> 12u);  
	PLAIN_TEXT[2u] = (uint8_t)((counter &  0x00000FF0u) >> 4u);   
	PLAIN_TEXT[3u] = (uint8_t)(((counter & 0x0000000Fu) << 4u)|((attribute_flags & 0xF0u) >> 4u)); 
	PLAIN_TEXT[4u] = (uint8_t)(attribute_flags & 0x0Fu) << 4u;
	//  ~127bit fill 0
	for(i=0u;i<11u;i++)
	{
		PLAIN_TEXT[5u+i] = 0u;
	}
	//128bit~255bit key id
	for(i=0u;i<16u;i++)
	{
		PLAIN_TEXT[16u+i] = new_key[i];
	}
	Res |= CSEC_DRV_EncryptCBC(CSEC_RAM_KEY,PLAIN_TEXT,32u,Iv,M2_out,2u);

	//****Calculate M3****
	//First, calculate K2 load it as RAM_KEY
	Res |= KDF(authorizing_key, KEY_UPDATE_MAC_C,K_out);
	Res |= CSEC_DRV_LoadPlainKey(K_out);
	//concatenate M1 and M2
	for(i=0u;  i<16u; i++)
		M1M2[i] = M1_out[i];
	for(i=16u; i<48u; i++)
		M1M2[i] = M2_out[i-16u];
	Res |= CSEC_DRV_GenerateMAC(CSEC_RAM_KEY,M1M2,384u,M3_out,2u);

	//****Calculate M4****
	//First, calculate K3 load it as RAM_KEY
	Res |= KDF(new_key, KEY_UPDATE_ENC_C,K_out);
	Res |= CSEC_DRV_LoadPlainKey(K_out);
	//calculate K4* = ENCECB(K3(CID¡¯(28 bits) | ¡°1¡±(1bit) | ¡°0¡­0¡±(99 bits)))
	M4_tmp[0u] = (uint8_t)((counter &  0x0FF00000u) >> 20u);
	M4_tmp[1u] = (uint8_t)((counter &  0x000FF000u) >> 12u);
	M4_tmp[2u] = (uint8_t)((counter &  0x00000FF0u) >> 4u);
	M4_tmp[3u] = (uint8_t)(((counter & 0x0000000Fu) << 4u)|0x08u);
	Res |= CSEC_DRV_EncryptCBC(CSEC_RAM_KEY,M4_tmp,16u,Iv,M4_star,2u);
	//0bit ~ 119bit UID
	Res |= CSEC_DRV_GetID(Challenge,UID,&Sreg,UID_MAC);
	for(i=0u;i<15u;i++)
	{
		M4_out[i] = UID[i];
	}
	//120bit ~ 1237bit KeyID(4bits)|AuthID(4bits)
	M4_out[15u] = (key_id << 4u)|(auth_key_id & 0x0Fu);
	//128bit ~ 255bit M4*
	for(i=0u;i<16u;i++)
	{
		M4_out[16u+i] = M4_star[i];
	}
	//****Calculate M5****
	Res |= KDF(new_key, KEY_UPDATE_MAC_C,K_out);
	Res |= CSEC_DRV_LoadPlainKey(K_out);
	Res |= CSEC_DRV_GenerateMAC(CSEC_RAM_KEY,M4_out,256u,M5_out,2u);
	return Res;

}

/*FUNCTION**********************************************************************
 *
 * Function Name : CalculateDbgAuth
 * Implements    :
 * END**************************************************************************/
uint16_t CalculateDbgAuth(uint8_t* MasterEcuKey,uint8_t * Challenge,uint8_t *DbgAuthOut)
{
	uint8_t K_out[16u];
	uint8_t UID[16u] = {0u};//UID just have 15 bytes
	uint8_t UID_MAC[16u] = {0u};
	uint8_t UidChallenge[16u]  = {0u, 1u, 2u, 3u, 4u, 5u, 6u, 7u, 8u, 9u, 10u, 11u, 12u, 13u, 14u, 15u};
	uint8_t DATA[32u];
	uint16_t Res=0u;
	uint8_t Sreg=0u;
	uint8_t i=0u;

	//step1 Calculate the Authorization
	Res = KDF(MasterEcuKey, DEBUG_KEY_C,K_out);
	Res = CSEC_DRV_LoadPlainKey(K_out);
	Res = CSEC_DRV_GetID(UidChallenge,UID,&Sreg,UID_MAC);
	for(i=0u; i<16u; i++)
		DATA[i] = Challenge[i];
	for(;i<32u;i++)
		DATA[i] = UID[i-16u];
	Res = CSEC_DRV_GenerateMAC(CSEC_RAM_KEY,DATA,248u,DbgAuthOut,2u);
	return Res;
}




