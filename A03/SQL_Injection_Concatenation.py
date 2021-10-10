@require_http_methods(["GET", "POST", "PUT", "DELETE"])
@user_is_authenticated
def user_view(request, user_id):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("User " + str(user_id) + "POST")
        user_id_form = form['user_id']
        table_name = User.objects.model._meta.db_table
        # The order by is_admin='0' moves admin to the first in list
        # which allows sql injection
        users = User.objects.raw(
            "SELECT * FROM %s WHERE user_id='%s' ORDER BY is_admin='0'"
            % (table_name, user_id_form))
