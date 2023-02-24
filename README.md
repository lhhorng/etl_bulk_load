# ETL Bulk Load

A simple way to perform ETL task is bulk load or full load. By transfer the source data(.xlsx,.sql...) to destination. 
In full load, the whole dataset is fully load by overwirte with new dataset. There are pros and cons in term of full load.
First, the full load method could be useful with the small data volumn and the one-time insert

![full load flow](https://github.com/lhhorng/etl_bulk_load/blob/f48d0ad9e08755b24e1e9e061c8c85c187298f23/full_load_flow_png.PNG)



## Example:
Dataset: (https://github.com/lhhorng/etl_bulk_load/tree/main/dataset)
Code: (https://github.com/lhhorng/etl_bulk_load/blob/main/main/etl_bulk_load.py)



