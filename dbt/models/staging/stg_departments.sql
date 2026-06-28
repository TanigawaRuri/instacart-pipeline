SELECT 
department_id,
department
FROM {{ source('raw', 'departments')}}