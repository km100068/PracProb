# PracProb
Problem workshop project

## Program modules

### Data extractor
Extracts data from `LinuxCommitData.cvs` from `data` folder as a list of `User` objects.

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
`getdata: List[User]`

