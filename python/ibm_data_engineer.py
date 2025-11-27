# from doggopyr.tools.helper_functions import Module as hf
"""
## 🛠️ The Senior Data Engineer Assessment: Marketing Attribution Pipeline

### **Scenario**

A major client needs a robust data platform to analyze digital marketing campaign performance. The core task is to process **massive clickstream data** (web logs) and **impression data** (ad views) to create a daily **Marketing Attribution Model** showing which campaigns led to customer purchases.

The expected volume is: **100 Billion** raw events per day, needing to be processed and loaded into a final data warehouse for reporting.

-----

## 📝 Part 1: System Design & Architecture (50% Weight)

Design the end-to-end architecture to meet the following requirements:

1.  **Ingestion:** Must handle a mix of high-volume, continuous streams (click data) and daily batched loads (purchase data).

Q: What are my sources of these two types of data? How can I pull data from them?
A: The source of the streaming data is a data broker tool like apache kafka or rabbit mq. If the source is apache kafka all we need is a kafka stream manager connector. If the stream broker uses a different protocol (like rabbit mq does) we would need to connect it to a kafka adapter and then sream the data into a pyspark dataframe we would then 'sink' into s3.

2.  **Processing:** Must use **AWS data integration and processing technologies (Glue, Athena, Redshift)** and **Spark**. The pipeline must ensure data is **de-duplicated** and joined before loading.
Q: Do you mean Spark the ETL tool? What is the use of Glue?


3.  **Storage:** Implement a **Lakehouse architecture** using **Amazon S3** as the foundational Data Lake storage.

Q: what other data do I get from each source? Geographical are and timestamp/ date? Is there a specific preference for a file type such as csv/ json?


4.  **Consumption:** The final, aggregated attribution table must reside in **Amazon Redshift** for fast analytical querying.

Q: Are all aws components located in the same environment? Do I have any authentication I need to do during the ETL flow?

### Task 1.1: Component Selection and Flow

1.  **Draw/Describe the architecture diagram.** Use specific AWS services mentioned (S3, Glue, Athena, Redshift).
2.  **Describe the role of each service in the pipeline:**
      * **Click Stream:** How is it ingested and staged in S3?
      * **Data Processing:** How is **AWS Glue (Spark)** used to read data from the S3 Lake, perform the attribution logic (join clicks/impressions to purchases), and write the result back?
      * **Data Loading:** How is the final structured data efficiently loaded from S3 into **Redshift**? (Hint: Consider COPY command or Glue's optimized Redshift connector).

### Task 1.2: Lakehouse Design and Data Governance

1.  **S3 Layering:** Define the three layers you would use in your S3 data lake (e.g., Raw, Staging/Silver, Curated/Gold). Justify the purpose of each.
2.  **Partitioning Strategy:** For the clickstream data (100 Billion events/day), recommend the optimal **partitioning strategy** (e.g., by date, time, or client ID). Explain *how* this strategy enhances performance in both **Spark (Glue)** processing and **Athena** querying.

-----

## 💻 Part 2: Spark/Python Optimization & Data Structures (30% Weight)

This task focuses on performance and your understanding of Spark's inner workings.

### Task 2.1: Spark Optimization and Joins

You have two Spark DataFrames:

  * `df_clicks`: 100 Billion records.
  * `df_campaigns`: **10,000 records** (metadata about the campaigns).

You need to enrich `df_clicks` by joining it to `df_campaigns` on the `campaign_id` key.

1.  **Identify the Optimal Join Strategy:** Given the huge size difference,
what is the most efficient type of Spark join to perform this enrichment?
2.  **Explain the Mechanism:** Describe the underlying concept/mechanism
(involving a specific **data structure**) that makes this join strategy faster
than a standard Sort-Merge Join. Explain why the average lookup time is near
**$O(1)$** for the larger DataFrame.
      * *(Hint: The answer should mention Hash Tables and memory distribution.)*

### Task 2.2: Python Generator vs. List (Conceptual)

Explain how a **Python Generator** (similar to a Linked List concept) is more
memory efficient than a standard Python **List** when dealing with reading a
massive, multi-gigabyte source file before loading it into Spark.

-----

## 📊 Part 3: SQL & Data Modeling (20% Weight)

The final requirement is a denormalized table in **Redshift** optimized for reporting.

### Task 3.1: Redshift Distribution and Sort Keys

You are defining the final, aggregated attribution table in Redshift: `ATTRIBUTION_SUMMARY`.

| Column Name | Data Type | Purpose |
| :--- | :--- | :--- |
| `reporting_date` | DATE | Used by all reports for time-series filtering. |
| `campaign_id` | INT | Used frequently for joining to Campaign Dimension Tables. |
| `user_id` | BIGINT | Used for detailed user analysis. |
| `conversion_count` | INT | The metric for reporting. |

1.  **Distribution Key (DISTKEY):** Which column would you choose as the `
DISTKEY`? Justify your choice based on how Redshift stores and processes data (i.e., minimizing data movement during joins).
2.  **Sort Key (SORTKEY):** Which column(s) would you choose as the `SORTKEY`?
Justify why this helps reporting queries run faster.

### Task 3.2: De-Duplication and Idempotency (SQL)

The raw clickstream data contains duplicates. Write a **SQL query** (or a
common table expression/CTE) that selects the **most recent unique record** for each `(user_id, click_timestamp)` combination, based on a single `event_id` column.

  * *(Hint: Use a Window Function like `ROW_NUMBER()` or `RANK()`).*

<!-- end list -->

```sql
-- Write your SQL solution here to find the latest unique click record.
-- Assume the table is named RAW_CLICKS.
```
"""
