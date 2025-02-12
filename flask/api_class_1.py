from flask import Flask,request
from string_to_num import string_to_num

app=Flask(__name__)
port=2200
@app.route('/',methods=['GET', 'POST'])
def home():
    return "Application is running"

@app.route('/add', methods=['POST','GET'])
def add_numbers() -> float:
    print(request.method)

    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return {"error": "Invalid JSON payload"}, 400
            v1 = data.get('v1')
            v2 = data.get('v2')
            # if the given data is not a number, convert it to a number
            if not isinstance(v1, (int, float)) or not isinstance(v2, (int, float)):
                    if isinstance(v1,str) and isinstance(v2,str):
                        # print("b3")
                        # using string_to_num function to convert string to number
                        v1 = string_to_num(v1)
                        v2 = string_to_num(v2)
                        result = v1 + v2
                        return {'result': result}, 200                  
                    elif isinstance(v1,str):
                        # print(v1,type(v2))
                        # print("b1")
                        v1 = string_to_num(v1)
                        result = v1 + v2
                        return {'result': result}, 200
                    elif isinstance(v2,str):
                        # print("b2")
                        v2 = string_to_num(v2)
                        result = v1 + v2
                        return {'result': result}, 200

                    else:
                        return {"error": "'v1' and 'v2' must be numbers"}, 500
            
            # elif v1.isnumeric() or v1.isnumeric() :
            #     status=200
            #     v1=float(v1)
            #     v2=float(v2)
            #     result = v1 + v2
            #     return {'result': result}, status
            # elif v1.isdigit() or v2.isdigit():
            #     status=200
            #     v1=int(v1)
            #     v2=int(v2)
            #     result = v1 + v2
            #     return {'result': result}, status
            
            else:
                result = v1 + v2
                return {'result': result}, 200
        except Exception as e:
            status=500
            return {"error": str(e)}, status

    elif request.method=='GET':
        status = 400
        try:
            # Extract numbers from query parameters
            numbers = request.args.getlist('nums')  # Retrieve list of 'nums' query parameters as floats
            print(numbers)
            if not numbers:
                return {"error": "No numbers provided. Use the 'nums' query parameter to pass numbers."}, status
            elif not isinstance(numbers, list):
                return {"error": "Invalid number"}, status
            elif any(isinstance(num, (str)) for num in numbers):
                for n in range(len(numbers)):
                    if isinstance(numbers[n], (int,float)):
                        continue
                    elif isinstance(numbers[n], str):
                        numbers[n] = string_to_num(numbers[n])
                        continue
                print(numbers)
                total = sum(numbers)
                return {'result': total}, 200
                    
            else:
                # for num in numbers:
                #     if isinstance(num,str):
                #         if isinstance(num,(int,float)):
                #             print("b1")
                #             continue
                #         else:
                #             print("b2")
                #             print(num)
                #         if any(num.isdigit() for n in num):
                #             num=string_to_num(num)
                # # Calculate the sum
                # print(numbers)
                print("SUMMATION BLOCK")
                b = [int(item) for item in numbers]
                status = 200
                total = sum(b)
                return {'result': total}, status
        except Exception as e:
            status = 500
            return {"error": str(e)}, status






    

# @app.route('/add', methods=['GET'])
# def add_multiple_numbers():
    


if __name__ == '__main__':
    app.run(debug=True,port=port,host='0.0.0.0')




