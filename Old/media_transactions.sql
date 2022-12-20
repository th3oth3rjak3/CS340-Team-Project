SELECT
    Media_Transactions.transaction_id,
    Media_Transactions.patron_id,
    Media_Transactions.transaction_type,
    Media_Transactions.employee_id,
    Media_Transactions.item_id,
    Counts.transaction_date
FROM
    Media_Transactions
INNER JOIN
    (
        SELECT DISTINCT
            Media_Transactions.patron_id, 
            Media_Transactions.item_id, 
            COALESCE(media_out.out_count, 0) AS Checkouts, 
            COALESCE(media_in.in_count,0) AS Checkins,
            media_out.transaction_date as transaction_date
        FROM 
            Media_Transactions 
        LEFT JOIN(
            SELECT 
                patron_id, 
                item_id, 
                transaction_type, 
                count(*) AS in_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions 
            WHERE
                transaction_type = "checkin" 
            GROUP BY 
                patron_id, item_id, transaction_type
            ) media_in 
        ON 
            Media_Transactions.patron_id = media_in.patron_id
        AND 
            Media_Transactions.item_id = media_in.item_id
        LEFT JOIN(
            SELECT
                patron_id,
                item_id,
                transaction_type,
                count(*) AS out_count,
                max(transaction_date) as transaction_date
            FROM 
                Media_Transactions
            WHERE 
                transaction_type = "checkout" 
            GROUP BY
                patron_id, 
                item_id, 
                transaction_type
            ) media_out
        ON
            Media_Transactions.patron_id = media_out.patron_id
        AND
            Media_Transactions.item_id = media_out.item_id
        HAVING
            Checkouts > Checkins
    ) Counts
ON
    Counts.patron_id = Media_Transactions.patron_id
AND
    Counts.item_id = Media_Transactions.item_id
AND
    Counts.transaction_date = Media_Transactions.transaction_date;