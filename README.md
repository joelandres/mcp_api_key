# mcp_api_key

##Run:
uvicorn server:app --reload --port 8002

##Test:
curl -X POST http://localhost:8002/tools/get_patient_age \
  -H "Content-Type: application/json" \
  -H "x-api-key: ############" \
  -d '{"birth_date":"1980-05-10"}'