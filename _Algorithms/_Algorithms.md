## #Contents 

```dataview
table
FROM #Algorithm 
WHERE file.name[0] = "_"
SORT file.name
```

```dataview
table algorithmType as Type
FROM #Algorithm 
WHERE file.name[0] != "_"
SORT file.name, algorithmType
```
