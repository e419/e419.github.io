# e419.github.io

How to base64

```python
import base64

with file('dest_path', 'wb+') as out_file:
    out_file.write(base64.b64encode('source_file'))
```
