-- Let's create a very simple sample bank accoutn database
use bank;

select * from accounts;


-- 1. start a new transaction
START TRANSACTION;

SELECT 
    @moneyAvailable:=IF(balance > 0, balance, 0) AS MONEY
FROM
    bank.accounts
WHERE
    account_number = 111112
        AND account_holder_surname = 'Smith';
        
--------
SET @TransferAmount = 50;

--------
UPDATE accounts 
SET 
    balance = balance - @TransferAmount
WHERE
    account_number = 111112
        AND account_holder_surname = 'Smith';
        
--------
UPDATE accounts 
SET 
    balance = balance + @TransferAmount
WHERE
    account_number = 111115
        AND account_holder_surname = 'Smith';

--------
select *
from accounts;

-- 2. (optional) Try Rollback to see how it works
-- ROLLBACK;

-- 3. commit changes 
COMMIT;



