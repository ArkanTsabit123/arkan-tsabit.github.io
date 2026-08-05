const { writeFileSync } = require('fs');
const { join } = require('path');

const knowledgeData = {
  documents: [
    // Professional Summary
    {
      id: 'profile_001',
      content: 'Arkan Tsabit is a Data Engineer with expertise in ETL pipelines, data warehousing, and cloud architecture. Certified Oracle Multicloud Architect, IBM Data Engineer, and Meta Database Engineer.',
      metadata: { category: 'profile' }
    },
    {
      id: 'profile_002',
      content: 'Arkan Tsabit specializes in building production-ready ETL pipelines that process millions of records in seconds with 100% data quality.',
      metadata: { category: 'profile' }
    },
    {
      id: 'profile_003',
      content: 'Arkan Tsabit transitioned from IT infrastructure and network engineering to data engineering through intensive self-study and hands-on projects.',
      metadata: { category: 'profile' }
    },
    // Skills
    {
      id: 'skill_001',
      content: 'Arkan Tsabit is proficient in Apache Airflow, PostgreSQL, DuckDB, Python, Pandas, Docker, Streamlit, Plotly, and Matplotlib.',
      metadata: { category: 'skills' }
    },
    {
      id: 'skill_002',
      content: 'Arkan Tsabit has expertise in ETL and ELT pipelines, data integration, star schema design, dimensional modeling, and data warehouse architecture.',
      metadata: { category: 'skills' }
    },
    // Projects
    {
      id: 'project_batchetl',
      content: 'BatchETL Pipeline: End-to-end ETL pipeline for NYC Taxi data. Processes 2.96M rows in under 30 seconds with 100% data quality. Uses Apache Airflow, PostgreSQL, Streamlit, and Docker.',
      metadata: { category: 'projects', name: 'BatchETL Pipeline' }
    },
    {
      id: 'project_uber',
      content: 'Uber Data Pipeline: ETL pipeline for NYC Uber/Taxi data. Uses Airflow orchestration, DuckDB warehouse, Star Schema with 4 dimension tables and 1 fact table.',
      metadata: { category: 'projects', name: 'Uber Data Pipeline' }
    },
    {
      id: 'project_amazon',
      content: 'Amazon Web Scraping: Python-based web scraper extracting 5 fields per product (Title, Price, Rating, Reviews, Availability). 95%+ success rate.',
      metadata: { category: 'projects', name: 'Amazon Web Scraping' }
    },
    {
      id: 'project_expense',
      content: 'Daily Expense Tracker: Full-stack expense app with CLI (12 menus) and GUI (6 tabs). SQLite with 5 tables, 277 test cases, 100% pass rate.',
      metadata: { category: 'projects', name: 'Daily Expense Tracker' }
    },
    // Certifications
    {
      id: 'cert_oracle_001',
      content: 'Oracle Multicloud Architect Professional - earned October 2025. Validates expertise in OCI and multicloud architecture.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_002',
      content: 'Oracle Generative AI Professional - earned October 2025. Validates expertise in generative AI and OCI GenAI services.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_003',
      content: 'Oracle AI Vector Search Certified Professional - earned October 2025. Validates expertise in AI vector search and vector databases.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_004',
      content: 'Oracle Autonomous Database Cloud Professional - earned October 2025. Validates expertise in Oracle Autonomous Database.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_005',
      content: 'Oracle Cloud Database Services Professional - earned October 2025. Validates expertise in Oracle cloud database services.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_006',
      content: 'Oracle OCI AI Foundations Associate - earned October 2025. Validates foundational knowledge in Oracle AI services.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_007',
      content: 'Oracle OCI Foundations Associate - earned October 2025. Validates foundational knowledge in Oracle Cloud Infrastructure.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_oracle_008',
      content: 'Oracle Data Platform Foundations Associate - earned October 2025. Validates foundational knowledge in Oracle Data Platform.',
      metadata: { category: 'certifications', provider: 'Oracle' }
    },
    {
      id: 'cert_ibm_001',
      content: 'IBM Data Engineering Professional Certificate - earned 2025. Validates expertise in data engineering and ETL pipelines.',
      metadata: { category: 'certifications', provider: 'IBM' }
    },
    {
      id: 'cert_meta_001',
      content: 'Meta Database Engineer Professional Certificate - earned 2025. Validates expertise in database design, SQL, and Python.',
      metadata: { category: 'certifications', provider: 'Meta' }
    },
    // Achievements
    {
      id: 'achievement_001',
      content: 'Top 108 Global in Oracle Race to Certification 2025.',
      metadata: { category: 'achievements' }
    },
    {
      id: 'achievement_002',
      content: 'Top 3 Indonesia in Oracle Race to Certification 2025.',
      metadata: { category: 'achievements' }
    },
    {
      id: 'achievement_003',
      content: 'Best Teacher Award at Satu Benih Boarding School 2025.',
      metadata: { category: 'achievements' }
    },
    // Work Experience
    {
      id: 'work_001',
      content: 'BRI SD-WAN (Feb 2026 - July 2026) - Level 2 Network Engineer. Managed network data migration across 100+ sites.',
      metadata: { category: 'experience' }
    },
    {
      id: 'work_002',
      content: 'SATU BENIH BOARDING SCHOOL (May 2025 - Feb 2026) - Database Administrator. Managed school databases (Dapodik, Sispena, BOS, ANBK).',
      metadata: { category: 'experience' }
    },
    {
      id: 'work_003',
      content: 'BEJAGOO COFFEE and EATERY (June 2020 - Mar 2024) - Business Manager. Analyzed sales data and optimized pricing strategies.',
      metadata: { category: 'experience' }
    },
    {
      id: 'work_004',
      content: 'Soekarno-Hatta International Airport (Feb 2016 - May 2020) - IT Terminal Service Support. Maintained IT infrastructure across 3 terminals.',
      metadata: { category: 'experience' }
    },
    // Contact
    {
      id: 'contact_001',
      content: 'Arkan Tsabit can be contacted at arkantsabit025@gmail.com or +62 81295709620. GitHub: github.com/ArkanTsabit123, LinkedIn: linkedin.com/in/arkan-tsabit.',
      metadata: { category: 'contact' }
    }
  ]
};

const outputPath = join(process.cwd(), 'knowledge-upload.json');
writeFileSync(outputPath, JSON.stringify(knowledgeData, null, 2));
console.log(`Saved ${knowledgeData.documents.length} documents to ${outputPath}`);
console.log('Now run: npx wrangler vectorize insert arkan-knowledge-base --file knowledge-upload.json');