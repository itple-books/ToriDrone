from time import sleep

# 코딩 라이더 모듈 불러오기
from CodingRider.drone import *
from CodingRider.protocol import *

# 메인 실행 부분
if __name__ == '__main__':

    drone1 = Drone()    # 1번째 Drone 객체 생성 후 변수(drone1)에 저장
    drone2 = Drone()    # 2번째 Drone 객체 생성 후 변수(drone2)에 저장
    drone3 = Drone()    # 3번째 Drone 객체 생성 후 변수(drone3)에 저장
    drone4 = Drone()    # 4번째 Drone 객체 생성 후 변수(drone4)에 저장
    drone5 = Drone()    # 5번째 Drone 객체 생성 후 변수(drone5)에 저장
    drone6 = Drone()    # 6번째 Drone 객체 생성 후 변수(drone6)에 저장
    drone7 = Drone()    # 7번째 Drone 객체 생성 후 변수(drone7)에 저장
    drone8 = Drone()    # 8번째 Drone 객체 생성 후 변수(drone8)에 저장


    # 연결된 각 드론과의 통신을 위한 시리얼 포트 연결 작업
    drone1.open("COM64")    # drone1 시리얼 포트 연결
    drone2.open("COM65")    # drone2 시리얼 포트 연결
    drone3.open("COM66")    # drone3 시리얼 포트 연결
    drone4.open("COM67")    # drone4 시리얼 포트 연결
    drone5.open("COM68")    # drone5 시리얼 포트 연결
    drone6.open("COM70")    # drone6 시리얼 포트 연결
    drone7.open("COM71")    # drone7 시리얼 포트 연결
    drone8.open("COM8")    # drone8 시리얼 포트 연결
    sleep(0.1)
    
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 255, 0)
        sleep(0.02)
    sleep(0.1)
    
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 255)
        sleep(0.02)
    sleep(0.1)
    
    # 이륙하기
    print("TakeOff")
    for i in range(30) :
        drone1.sendTakeOff()    # drone1 이륙
        drone2.sendTakeOff()    # drone2 이륙
        drone3.sendTakeOff()    # drone3 이륙
        drone4.sendTakeOff()    # drone4 이륙
        drone5.sendTakeOff()    # drone5 이륙
        drone6.sendTakeOff()    # drone6 이륙
        drone7.sendTakeOff()    # drone7 이륙
        drone8.sendTakeOff()    # drone8 이륙
        sleep(0.02)
    
    for i in range(2, 0, -1):   # 이륙하는동안 2초 카운트
        print("{0}".format(i))
        sleep(1)

    # 호버링하기
    print("Hovering")
    for i in range(1, 0, -1):   # 3초동안 호버링
        print("{0}".format(i))
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        drone3.sendControlWhile(0, 0, 0, 0, 1000)   # drone3 호버링(1초)
        drone4.sendControlWhile(0, 0, 0, 0, 1000)   # drone4 호버링(1초)
        drone5.sendControlWhile(0, 0, 0, 0, 1000)   # drone5 호버링(1초)
        drone6.sendControlWhile(0, 0, 0, 0, 1000)   # drone6 호버링(1초)
        drone7.sendControlWhile(0, 0, 0, 0, 1000)   # drone7 호버링(1초)
        drone8.sendControlWhile(0, 0, 0, 0, 1000)   # drone8 호버링(1초)
        sleep(0.1)

    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        sleep(0.02)
    sleep(0.1)
    
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        sleep(0.02)
    sleep(0.1)
    
#4기체의 드론만 고도 상승
    print("4개의 기체 고도 상승")
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone1 0.5m 상승
        drone2.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone2 0.5m 상승
        drone3.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone3 0.5m 상승
        drone4.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone4 0.5m 상승
        sleep(0.02)

    for i in range(1, 0, -1):   #1초 대기
        print("{0}".format(i))
        sleep(1)
    
    #led 색 변경
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        sleep(0.02)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        sleep(0.02)
    sleep(0.1)
    
    #고도 상승했던 4개의 기체는 0.5미터 하강 / 나머지 4개의 기체는 고도 상승
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone1 0.5m 하강
        drone2.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone2 0.5m 하강
        drone3.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone3 0.5m 하강
        drone4.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone4 0.5m 하강
        drone5.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone5 0.5m 상승
        drone6.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone6 0.5m 상승
        drone7.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone7 0.5m 상승
        drone8.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone8 0.5m 상승
        
    for i in range(2, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
        #led 색 변경
        
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        sleep(0.02)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        sleep(0.02)
    sleep(0.1)
    
    #고도 상승했던 4개의 기체는 0.5미터 하강 / 나머지 4개의 기체는 고도 상승 2
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone1 0.5m 상승
        drone2.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone2 0.5m 상승
        drone3.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone3 0.5m 상승
        drone4.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone4 0.5m 상승
        drone5.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone5 0.5m 하강
        drone6.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone6 0.5m 하강
        drone7.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone7 0.5m 하강
        drone8.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone8 0.5m 하강
        
    for i in range(2, 0, -1):   # 1초 대기
        print("{0}".format(i))
        sleep(1)
        
    #led 색 변경
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        sleep(0.02)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        sleep(0.02)
    sleep(0.1)
    
    #고도 상승했던 4개의 기체는 0.5미터 하강 / 나머지 4개의 기체는 고도 상승3
    for i in range(30) :
        drone1.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone1 0.5m 하강
        drone2.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone2 0.5m 하강
        drone3.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone3 0.5m 하강
        drone4.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone4 0.5m 하강
        drone5.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone5 0.5m 상승
        drone6.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone6 0.5m 상승
        drone7.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone7 0.5m 상승
        drone8.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone8 0.5m 상승
        
    for i in range(2, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
        #led 색 변경
        
    print("led 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        sleep(0.02)
    print("led 다리색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        sleep(0.02)
    sleep(0.1)
    
    #고도 상승했던 4개의 기체는 0.5미터 하강 / 나머지 4개의 기체는 고도 상승4
    for i in range(30) :
        drone1.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone1 0.5m 상승
        drone2.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone2 0.5m 상승
        drone3.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone3 0.5m 상승
        drone4.sendControlPosition(0, 0, 0.5, 0.5, 0, 0) #drone4 0.5m 상승
        drone5.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone5 0.5m 하강
        drone6.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone6 0.5m 하강
        drone7.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone7 0.5m 하강
        drone8.sendControlPosition(0, 0, -0.5, 0.5, 0, 0) #drone8 0.5m 하강
        
    for i in range(2, 0, -1):   # 1초 대기
        print("{0}".format(i))
        sleep(1)
        
    #좌우 군집비행
    print("다리 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)

        sleep(0.02)
    sleep(0.1)
    print("몸통 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)     
        sleep(0.02)
    sleep(0.1)
    
    print("좌우 군집비행 시작")
    for i in range(30) :
        drone1.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone1 0.5m 좌로 이동
        drone2.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone2 0.5m 좌로 이동
        drone3.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone3 0.5m 좌로 이동
        drone4.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone4 0.5m 좌로 이동
        drone5.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone5 0.5m 우로 이동
        drone6.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone6 0.5m 우로 이동
        drone7.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone7 0.5m 우로 이동
        drone8.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone8 0.5m 우로 이동
        sleep(0.02)

    for i in range(3, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
        
    #좌우 군집비행
    for i in range(30) :
        drone1.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone1 0.5m 우로 이동
        drone2.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone2 0.5m 우로 이동
        drone3.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone3 0.5m 우로 이동
        drone4.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone4 0.5m 우로 이동
        drone5.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone5 0.5m 좌로 이동
        drone6.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone6 0.5m 좌로 이동
        drone7.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone7 0.5m 좌로 이동
        drone8.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone8 0.5m 좌로 이동
        sleep(0.02)   
    sleep(0.1)
    
    print("다리 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)

        sleep(0.02)
    sleep(0.1)
    print("몸통 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)     
        sleep(0.02)
    sleep(0.1)


    for i in range(3, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
    
     #좌우 군집비행
    for i in range(30) :
        drone1.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone1 0.5m 우로 이동
        drone2.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone2 0.5m 우로 이동
        drone3.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone3 0.5m 우로 이동
        drone4.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone4 0.5m 우로 이동
        drone5.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone5 0.5m 좌로 이동
        drone6.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone6 0.5m 좌로 이동
        drone7.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone7 0.5m 좌로 이동
        drone8.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone8 0.5m 좌로 이동
        sleep(0.02)

    for i in range(3, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
        
    print("다리 색 변경")
    for i in range(30) :   
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 0, 0, 255)

        sleep(0.02)
    sleep(0.1)
    print("몸통 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 0, 0, 255)     
        sleep(0.02)
    sleep(0.1)
    #좌우 군집비행
    for i in range(30) :
        drone1.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone1 0.5m 좌로 이동
        drone2.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone2 0.5m 좌로 이동
        drone3.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone3 0.5m 좌로 이동
        drone4.sendControlPosition(0, 0.5, 0, 0.5, 0, 0) #drone4 0.5m 좌로 이동
        drone5.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone5 0.5m 우로 이동
        drone6.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone6 0.5m 우로 이동
        drone7.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone7 0.5m 우로 이동
        drone8.sendControlPosition(0, -0.5, 0, 0.5, 0, 0) #drone8 0.5m 우로 이동
        sleep(0.02)

    for i in range(3, 0, -1):   # 3초 대기
        print("{0}".format(i))
        sleep(1)
        
    
    #led 색깔 변경
    print("다리 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.TeamRgbHold, 255, 255, 0, 0)
    sleep(0.1)
    print("몸통 색 변경")
    for i in range(30) :
        drone1.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone2.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone3.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone4.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone5.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone6.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone7.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)
        drone8.sendLightModeColor(LightModeDrone.BodyHold, 255, 255, 0, 0)     
        sleep(0.02)
    sleep(0.3)
    # 착륙하기
    print("Landing")
    for i in range(30) :
        drone1.sendLanding()    # drone1 착륙
        drone2.sendLanding()    # drone2 착륙
        drone3.sendLanding()    # drone3 착륙
        drone4.sendLanding()    # drone4 착륙
        drone5.sendLanding()    # drone5 착륙
        drone6.sendLanding()    # drone6 착륙
        drone7.sendLanding()    # drone7 착륙
        drone8.sendLanding()    # drone8 착륙
        sleep(0.02)
        
    for i in range(3, 0, -1):   # 착륙 및 하강하는동안 3초 카운트
        print("{0}".format(i))
        sleep(1)


    # 시리얼 포트 닫기 작업(모든 명령이 완료되면 시리얼 포트를 닫아줌.)
    drone1.close()  # drone1 시리얼 포트 닫기
    drone2.close()  # drone2 시리얼 포트 닫기
    drone3.close()  # drone3 시리얼 포트 닫기
    drone4.close()  # drone4 시리얼 포트 닫기
    drone5.close()  # drone5 시리얼 포트 닫기
    drone6.close()  # drone6 시리얼 포트 닫기
    drone7.close()  # drone7 시리얼 포트 닫기 
    drone8.close()  # drone8 시리얼 포트 닫기