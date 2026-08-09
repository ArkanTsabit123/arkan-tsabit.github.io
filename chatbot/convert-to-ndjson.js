const { readFileSync, writeFileSync } = require('fs');
const { join } = require('path');

// Read the JSON file
const jsonPath = join(process.cwd(), 'knowledge-upload.json');
const jsonData = JSON.parse(readFileSync(jsonPath, 'utf-8'));

// Convert to NDJSON WITHOUT vectors
// Cloudflare will generate the embeddings automatically
const ndjsonContent = jsonData.documents.map(doc => {
    return JSON.stringify({
        id: doc.id,
        metadata: doc.metadata || {}
        // NO 'values' field - Cloudflare generates embeddings
    });
}).join('\n');

// Write the NDJSON file
const outputPath = join(process.cwd(), 'knowledge-upload.ndjson');
writeFileSync(outputPath, ndjsonContent, 'utf-8');

