

#ifndef CSEC_FUNCTIONS_H_
#define CSEC_FUNCTIONS_H_
#include "cpu.h"

/*!
 * @brief Calculate M1 to M5.
 *
 * @param[in] authorizing_key: authorize key
 * @param[in] new_key:The key will be updated.
 * @param[in] auth_key_id:Authorize key ID.
 * @param[in] auth_key_id:The updated key ID.
 * @param[in] counter:update counter.
 * @param[in] attribute_flags:updated key attribute.
 * @param[out] M1_out~M5_out:M1~M5 output
 * @return Error Code after command execution. Output parameters are valid if
 * the error code is STATUS_SUCCESS.
 */
uint16_t CalculateM1ToM5(uint8_t *authorizing_key, uint8_t *new_key, uint8_t auth_key_id, uint8_t key_id, uint32_t counter, uint8_t attribute_flags,
						          uint8_t *M1_out, uint8_t *M2_out, uint8_t *M3_out, uint8_t *M4_out, uint8_t *M5_out);

/*!
 * @brief Calculate CSEc reset to factory authorize key.
 *
 * @param[in] MasterEcuKey: master ecu key
 * @param[in] Challenge:ramdom value
 * @param[out] DbgAuthOut: the output authorize key.
 * @return Error Code after command execution. Output parameters are valid if
 * the error code is STATUS_SUCCESS.
 */
uint16_t CalculateDbgAuth(uint8_t* MasterEcuKey,uint8_t * Challenge,uint8_t *DbgAuthOut);


#endif /* CSEC_FUNCTIONS_H_ */
