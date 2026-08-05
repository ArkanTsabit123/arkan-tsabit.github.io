#upload-knowledge.sh
# ============================================================
# UPLOAD KNOWLEDGE BASE VIA WRANGLER
# ============================================================

echo "============================================================"
echo "KNOWLEDGE BASE UPLOADER"
echo "============================================================"

# Check if Wrangler is available
if ! command -v npx wrangler &> /dev/null; then
    echo "Wrangler not found. Please install it first:"
    echo "npm install -g wrangler"
    exit 1
fi

# Check if knowledge file exists
if [ ! -f "knowledge-upload.json" ]; then
    echo "knowledge-upload.json not found."
    echo "Run upload-knowledge.js first to generate the file."
    exit 1
fi

# Upload to Vectorize
echo "Uploading knowledge base to Vectorize..."
npx wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.json

echo "============================================================"
echo "UPLOAD COMPLETE"
echo "============================================================"