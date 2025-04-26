@app.route('/tokenPage')
@token_required
def tokenPage(current_user):
    token = request.cookies.get('token')
    return render_template('TokenPage.html', token=token)