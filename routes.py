@app.route('/dashboard')
@login_required
def dashboard():
    entries = TimeEntry.query.filter_by(user_id=current_user.id).all()
    total_hours = sum([entry.hours for entry in entries])
    return render_template('dashboard.html', entries=entries, total_hours=total_hours)
