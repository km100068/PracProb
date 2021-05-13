# PracProb
Problem workshop project

## Program modules

### Data extractor
Extracts data from `LinuxCommitData.cvs` situated in `data` folder.

#### Types
```
User extends typing.TypedDict
    date: datetime.date
    commits: int
    additions: int
    deletions: int
    id: int
```


#### Functions
`get_data: List[User]` - extracts data as a list of `User` objects

`get_data_as_numpy_arrays() -> List[numpy.longlong]` - extract data as numpy arrays of `longlong` type 

