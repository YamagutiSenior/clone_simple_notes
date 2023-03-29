import os
from notes import note

if __name__ == "__main__":
    aws_key_id = "AKIAIOSFODNN7EXAMPLE"
    pat = "glpat-7mb3gL5p5FwkVqjkvnNt"
    port = int(os.environ.get("PORT", 5000))
    note.run(host='0.0.0.0', port=port, debug=False)