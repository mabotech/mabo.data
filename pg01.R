
library(RPostgreSQL)


query <- function(){
    drv <- dbDriver("PostgreSQL")
    con <- dbConnect(drv, user = "mabotech",password = "mabouser", port = 6432, dbname = "maboss")
    res <- dbSendQuery(con, statement = paste(
                          "SELECT  station, state_start, state_stop, duration  from public.engine_test limit 10"))
    # we now fetch the first 100 records from the resultSet into a data.frame
    data1 <- fetch(res, n = 5)   
    dim(data1)

    print(data1)

    dbHasCompleted(res)

    # let's get all remaining records
    data2 <- fetch(res, n = -1)

    return(data2)
}


v <- query()

print(v)