from flask import Blueprint, request, jsonify

detailAPI = Blueprint('detail', __name__)

# API 작성하는 부분
# @detailAPI.route('/memo', methods=['GET'])
# def listing():
#     sample_receive = request.args.get('sample_give')
#     print(sample_receive)
#     return jsonify({'msg':'GET 연결되었습니다!'})
#
# @detailAPI.route('/memo', methods=['POST'])
# def saving():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg':'POST 연결되었습니다!'})