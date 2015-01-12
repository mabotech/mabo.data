

library(influxdb)


library(ggplot2)
library(scales)

query <- function (){

    query <- 'SELECT sum(a) as sum_a, sum(b) as sum_b, sum(c) as sum_c FROM lab2 where time > now() -1h';

    # time_precision=c("s", "m", "u")
    # order no by

    results <- influxdb_query('192.168.147.140', 8086, 'root', 'root', 'monitor',
                                           'SELECT a  FROM lab2 where time > now() -2h order asc', 's');
    return(results$lab2);
}

#

df1 <- query()

df1$time <-  as.POSIXct(df1$time, origin ="1970-01-01 00:00:00", format = "%Y-%m-%d %H:%M:%S")

df1

 plt <- ggplot(data = df1,  aes(x=time,y = a )) +
    
        geom_point(color="red", shape=0) + 
        geom_line( )
        #    scale_x_datetime( format = "%H:%M:%S")



ggsave("a2.png", width=8, height=2)

