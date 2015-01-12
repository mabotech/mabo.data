
library(RPostgreSQL)

library(ggplot2)
library(scales)

query <- function(){
    drv <- dbDriver("PostgreSQL")
    con <- dbConnect(drv, user = "mabotech",password = "mabouser", port = 6432, dbname = "maboss")
    res <- dbSendQuery(con, statement = paste(
                          "SELECT  station, state_start, state_stop, duration  from public.engine_test where station = 'TestZone6_TC10' and state_start>'2010-12-20 19:35:00' limit 20"))
    # we now fetch the first 100 records from the resultSet into a data.frame
    data1 <- fetch(res, n = -1)   
    
    #print(dim(data1))

    #print(data1)

    #dbHasCompleted(res)

    # let's get all remaining records
   # data2 <- fetch(res, n = -1)

    #return(data2)
    return(data1)
}


df1<- query()

print(df1)

 plt <- ggplot(data = df1   ) +
    
        geom_point(aes(x=state_start,y = log(duration)), color="red", shape=0) + 
        geom_line( aes(x=state_start,y = log(duration)) , color="red")        
        #geom_point(aes(x=state_stop,y = log(duration)), color="blue", shape=0) + 
        #geom_line( aes(x=state_stop,y = log(duration)), color="blue" )
        
        
        #    scale_x_datetime( format = "%H:%M:%S")



ggsave("output/pg01.png", width=8, height=2)
