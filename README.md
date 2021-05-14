# PracProb
Problem workshop project

## Program modules

### Data extractor
Extracts data from `LinuxCommitData.cvs` situated in `data` folder.

#### Types
```
class User(typing.TypedDict):
    date: datetime.date
    commits: int
    additions: int
    deletions: int
    id: int
```


#### Functions
`get_data: List[User]` - extracts data as a list of `User` objects

`get_data_as_numpy_arrays() -> List[numpy.longlong]` - extracts data as numpy arrays of `longlong` type.
Each array contain the following elements:
- 0 - id,
- 1 - date as a unix timestamp,
- 2 - commits amount,
- 3 - additions amount,
- 4 - deletions amount.

