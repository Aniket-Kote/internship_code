from flask import Flask,request
from string_to_num import string_to_num

app=Flask(__name__)
port=2200
@app.route('/',methods=['GET', 'POST'])
def home():
    return "Application is running"

@app.route('/add', methods=['POST','GET'])
def add_numbers():
    print(request.method)

    if request.method == 'POST':
        status=400
        try:
            data = request.get_json()
            if not data:
                return {"error": "Invalid JSON payload"}, status
            v1 = data.get('v1')
            v2 = data.get('v2')
            if not isinstance(v1, (int, float)) or not isinstance(v2, (int, float)):
                if any(v1.isdigit() for num1 in v1) or any(v2.isdigit() for num2 in v2):
                    status=200
                    v1=string_to_num(v1)
                    v2=string_to_num(v2)
                    result = v1 + v2
                    return {'result': result}, status
                else:
                    return {"error": "'v1' and 'v2' must be numbers"}, status
            elif v1.isnumeric() or v1.isnumeric() :
                status=200
                v1=float(v1)
                v2=float(v2)
                result = v1 + v2
                return {'result': result}, status
            # elif v1.isdigit() or v2.isdigit():
            #     status=200
            #     v1=int(v1)
            #     v2=int(v2)
            #     result = v1 + v2
            #     return {'result': result}, status
            
            else:
                status=200
                result = v1 + v2
                return {'result': result}, status
        except Exception as e:
            status=500
            return {"error": str(e)}, status

    elif request.method=='GET':
        status = 400
        try:
            # Extract numbers from query parameters
            numbers = request.args.getlist('nums', type=float)  # Retrieve list of 'nums' query parameters as floats
            print(numbers)
            if not numbers:
                return {"error": "No numbers provided. Use the 'nums' query parameter to pass numbers."}, status
            elif not isinstance(numbers, list):
                return {"error": "Invalid number"}, status
            else:
                # Calculate the sum
                status = 200
                total = sum(numbers)
                return {'result': total}, status
        except Exception as e:
            status = 500
            return {"error": str(e)}, status






    

# @app.route('/add', methods=['GET'])
# def add_multiple_numbers():
    


if __name__ == '__main__':
    app.run(debug=True,port=port,host='0.0.0.0')




