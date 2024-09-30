from pathlib import Path

from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent


# Load a model
model = YOLO(BASE_DIR / "best.pt")


def solve_cap(path):
    result = model.predict(path)
    summary = result[0].summary()
    sorted_res = sorted(summary, key=lambda x: float(x.get("box").get("x1")))
    first_num = ""
    second_num = ""
    operator = ""
    for ob in sorted_res:
        if "plus" == ob.get("name"):
            operator = "plus"
        elif "minus" == ob.get("name"):
            operator = "minus"
        elif operator:
            second_num += ob.get("name")
        else:
            first_num += ob.get("name")

        if operator and first_num and second_num:
            first_num = int(first_num)
            second_num = int(second_num)
            res = (
                first_num + second_num if operator == "plus" else first_num - second_num
            )
            return str(res)
