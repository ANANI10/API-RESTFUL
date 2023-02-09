from flask import request, json,jsonify
from model import Order
from app import app
from config import db

with app.app_context():
    db.create_all()

@app.route('/Order/add', methods=['POST'])

def add_Order():
    try:
        json = request.json
        print(json)
        createDate = json['createDate']
        if createDate and request.method=='POST':
            order = Order(createDate=createDate)
            db.session.add(order)
            db.session.commit()
            resultat = jsonify('order ajouté avec succes')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code status":404 , "message":"error"}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/Order/delete',methods=['GET'])
def delete_Order():
    try:
        json = request.json
        id = json['id']
        order = Order.query.filter_by(id=id).first()
        db.session.delete(order)
        db.session.commit()
        resultat = jsonify('suppression de order')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code status":400 , "message":"erreur" }
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/Order/all',methods=['GET'])   
def all_Order():
    try:
        
        orders = Order.query.all()
        data = [{"id":orders.id,"createDate":Order.createDate}]
        resultat = jsonify({"code status ":400, "users":data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code status":404 , "message":"error"}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/Order/delete',methods=['POST','GET'])
def update_Order():
    try:
        json = request.json
        id = json['id']
        createDate = json['createDate']
        if id and createDate and request.method=='POST':
            order = Order.query.filter_by(id=id).first()
            order.createDate = createDate
            db.session.commit()
            resultat = jsonify('Update de order')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code status":400 , "message":"erreur" }
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ == '__main__'):
    app.run()