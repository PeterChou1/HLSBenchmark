import scalehls
import io
import mlir.ir

# Traverse all functions in MLIR.
# Parse C/C++ into MLIR.
mod = mlir.ir.Module.parse(fin, ...)
# Emit transformed MLIR to HLS C++.
buf = io.StringIO()
scalehls.emit_hlscpp(mod, buf)