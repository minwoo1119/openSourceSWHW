def cm_to_m(cm):
  meters = cm / 100
  return meters

cm_input = float(input("변환할 센티미터(cm) 값을 입력하세요: "))
print(cm_to_m(cm_input))