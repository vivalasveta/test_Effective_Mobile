SELECT 
    id, 
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position 
FROM examination
ORDER BY position, id

#Использовала RANK(), так как при одинаковых баллах абитуриенты должны делить место (1, 1, 3, 4...).
Если требуется нумерация без пропусков можно заменить на DENSE_RANK().
