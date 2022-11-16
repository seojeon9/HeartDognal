CREATE OR REPLACE PROCEDURE UPDATE_PROCESS
IS
BEGIN
    UPDATE ROADDOG_INFO
    SET PROCESS_ST = '���� (�ȶ���)'
    WHERE HAPPEN_DT < TO_CHAR(SYSDATE-15, 'YYYYMMDD') AND PROCESS_ST = '��ȣ��';
    COMMIT;
END;
/
EXEC UPDATE_PROCESS;
/
select * from roaddog_info
where HAPPEN_DT < TO_CHAR(SYSDATE-15, 'YYYYMMDD') AND PROCESS_ST = '��ȣ��';
/
--DECLARE
--X NUMBER;
--BEGIN
--SYS.DBMS_JOB.SUBMIT(
--    job => X,
--    what => 'UPDATE_PROCESS',
--    next_date => to_date('11-14-2022 12:00:00', 'dd/mm/yyyy h:i:s'),
--    interval => 'SYSDATE +1',
--    no_parse => FALSE
--);
--SYS.DBMS_OUTPUT.PUT_LINE('job Number is: ' || to_char(x));
--COMMIT;
--END;
/
BEGIN
    DBMS_SCHEDULER.CREATE_JOB (
        JOB_NAME => 'UPDATE_PROCESS_JOB'
        , START_DATE => TRUNC(SYSDATE+1)+6/24
        , REPEAT_INTERVAL => 'FREQ=DAILY;INTERVAL=1'
        , END_DATE => NULL
        , JOB_CLASS => 'DEFAULT_JOB_CLASS'
        , JOB_TYPE => 'STORED_PROCEDURE'
        , JOB_ACTION => 'UPDATE_PROCESS'
        , COMMENTS => '����� ���� ��ȯ JOB'
    );
    DBMS_SCHEDULER.ENABLE('UPDATE_PROCESS_JOB');
END;
/
BEGIN
DBMS_SCHEDULER.DROP_JOB(job_name => 'UPDATE_PROCESS_JOB', defer => false,force => false);
END;
/
-- �� Ȯ��
SELECT JOB_NAME, JOB_STYLE, JOB_CREATOR, JOB_TYPE, JOB_ACTION, SCHEDULE_TYPE, START_DATE, REPEAT_INTERVAL, ENABLED, STATE FROM user_scheduler_jobs;
/
-- �� �α� Ȯ��
select * from user_scheduler_job_log where job_name='UPDATE_PROCESS_JOB';
/
-- �ߺ��Ǵ� �����ȣ (���� ���� ģ��) delete
DELETE from roaddog_info a WHERE ROWID < (SELECT MAX(ROWID) FROM roaddog_info b
WHERE b.desertion_no = a.desertion_no);
/
-- �ߺ��Ǵ� ģ�� Ȯ��
/
select count(*) from roaddog_info a WHERE ROWID < (SELECT MAX(ROWID) FROM roaddog_info b
WHERE b.desertion_no = a.desertion_no);
/
select * from roaddog_info where desertion_no = '448535202201935';