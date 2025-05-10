# 🟡 Processed `.cast` Files

This folder contains intermediate `.cast` files created after applying simulation transformations:

- `demo-typed.cast`: Simulated human typing from `simulate-typing.py`
- `demo-guru.cast`: Extended CLI simulation from `simulate-guru-extended.py`

These files are used as input for `svg-term` rendering into `.svg`, `.mp4`, or `.mov`.

## Workflow

```
assets/raw/demo.cast
  └── simulate-typing.py → demo-typed.cast
        └── simulate-guru-extended.py → demo-guru.cast
```

All files here are safe to delete and regenerate using the `Makefile`.
