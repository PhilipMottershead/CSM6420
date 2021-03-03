# Seminar 4

## Peer to Peer Consistency

- Overall it won't be consistent until the change is propagated throughout the system
  - Neither Sequential
	- Not useful
  - eventual consistency works
	- Can cause major distributions
	- Replica node are unreliable

- Need to implement system that find a middle ground
  - Probabilistic consistency
    - only guarantees consistency on most nodes
  - time-bounded consistency
	- uniform temporal constraint on inconsistency

##  Node Failure in Sharding

- Replication
  - Allow copies to be uniformly distributed
  - Allows access to the data
- Backup
  - Would allow nodes to be created with backups of the data that is down
- Monitoring
  - Know when the nodes go down or have issues
- Planning
  - Plan for failure and work how to deal with the issues  

## Problems sharding and peer-to-peer replication

- AP
	- Consistency issues
		- Need methods to mitigate impact
	- Maintenance issues
		- replication
		- node maintenance

## Difference ETL and ELT models

### The five critical differences of ETL vs ELT:

1.  ETL is the Extract, Transform, and Load process for data. ELT is Extract, Load, and Transform process for data.
2.  In ETL, data moves from the data source to staging into the data warehouse.
3.  ELT leverages the data warehouse to do basic transformations. There is no need for data staging.
4.  ETL can help with data privacy and compliance by cleaning sensitive and secure data even before loading into the data warehouse.
5.  ETL can perform sophisticated data transformations and can be more cost-effective than ELT.

![undefined](https://cdn.filestackcontent.com/auto_image/compress/LjY9fP8fQWyBQ4aVlLy7)

![undefined](https://cdn.filestackcontent.com/auto_image/compress/esfcZz4QqSrriADPU2i7)

## ELT
- High Speed
- Low-Maintenance
- Quicker Loading