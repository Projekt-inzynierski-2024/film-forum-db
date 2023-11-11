#!/bin/bash
(/opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Recovery is complete." &&
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -i /backup.sql &&
sleep infinity & wait
