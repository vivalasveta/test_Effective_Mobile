1 задание:
    
SELECT 
    id, 
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position 
FROM examination
ORDER BY position, id
#Использовала RANK(), так как при одинаковых баллах абитуриенты должны делить место (1, 1, 3, 4...).
#Если требуется нумерация без пропусков можно заменить на DENSE_RANK().

2 задание:
Минимально 30 и максимально 50 строк

3 задание:

SELECT account_id, SUM(amount) AS total_purchases
FROM transaction
WHERE transaction_date >= CURRENT_DATE - 30
GROUP BY account_id
HAVING SUM(amount) < 5000 

или
    
SELECT account_id, SUM(amount) AS total_purchases
FROM transaction
WHERE transaction_date >= CURRENT_DATE - INTERVAL '30 days'
  AND type = ''  -указываем тип списания
GROUP BY account_id
HAVING SUM(amount) < 5000
