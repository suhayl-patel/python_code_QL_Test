@classmethod
def hits_by_ip(cls, ip, col='*'):
    table_name = cls.objects.model._meta.db_table
    cmd = "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC" % (
        col, table_name, ip)
    with connection.cursor() as cursor:
        cursor.execute(cmd)
        raw = cursor.fetchall()
    formated = Analytics.format_raw_sql(cmd, raw)
    return formated
