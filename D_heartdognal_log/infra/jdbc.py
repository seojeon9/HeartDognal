from enum import Enum
from infra.spark_session import get_spark_session

class DataWarehouse(Enum):
    URL ='jdbc:oracle:thin:@decorona_high?TNS_ADMIN=/home/big/study/db/Wallet_DECORONA'
    PROPS={
        'user':'dw_de'
       ,'password':'123qwe!@#QWE'
    }

class DataMart(Enum):
    URL ='jdbc:oracle:thin:@decorona_high?TNS_ADMIN=/home/big/study/db/Wallet_DECORONA'
    PROPS={
        'user':'dm_de'
       ,'password':'123qwe!@#QWE'
    }

def save_data(config, dataframe, table_name):
    dataframe.write.jdbc(url=config.URL.value
                        , table=table_name
                        , mode='append'
                        , properties=config.PROPS.value)

def overwrite_data(config, dataframe, table_name):
    dataframe.write.jdbc(url=config.URL.value
                        , table=table_name
                        , mode='overwrite'
                        , properties=config.PROPS.value)

def find_data(config, table_name):
    return get_spark_session().read.jdbc(url=config.URL.value
                                , table=table_name
                                , properties=config.PROPS.value)