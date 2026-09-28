import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///database.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Catatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    isi = db.Column(db.Text, nullable=False)
    dibuat_pada = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Catatan {self.judul}>'


@app.route('/')
def index():
    semua_catatan = Catatan.query.order_by(Catatan.dibuat_pada.desc()).all()
    return render_template('index.html', catatan_list=semua_catatan)


@app.route('/tambah', methods=['POST'])
def tambah_catatan():
    catatan_baru = Catatan(
        judul=request.form['judul'],
        isi=request.form['isi']
    )
    db.session.add(catatan_baru)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['POST'])
def edit_catatan(id):
    catatan = Catatan.query.get_or_404(id)
    catatan.judul = request.form['judul']
    catatan.isi = request.form['isi']
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/hapus/<int:id>')
def hapus_catatan(id):
    catatan = Catatan.query.get_or_404(id)
    db.session.delete(catatan)
    db.session.commit()
    return redirect(url_for('index'))


# Membuat tabel otomatis saat aplikasi pertama kali dijalankan
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
