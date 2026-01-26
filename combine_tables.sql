SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
From Person P
LEFT JOIN Address a
    ON p.personId = a.personId;
