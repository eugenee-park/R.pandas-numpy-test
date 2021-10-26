1. 설치

pip install numpy (python -m pip install numpy)
pip install pandas
pip install sqlalchemy
pip install matplob


2. fish csv

프로젝트 추가


3. pandas로 csv로드

bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()


4. 시각화

    plt.scatter(bream_length, bream_weight)
    plt.scatter(smelt_length, smelt_weight)
    plt.show()
    
    
5. 데이터 정제하기

np.concatenate((bream_length, smelt_length))
np.column_stack((fish_length, fish_weight))


6. 타겟 데이터 만들기

fish_target = np.concatenate((np.ones(35), np.zeros(14)))


7. 셔플하기

인덱스 만들기
indexes = np.arange(49)
인덱스를 셔플하기
np.random.shuffle(indexes)
실재데이터를 인덱스로 섞기
fish_data = fish_data[indexes]
fish_target = fish_target[indexes]


8. 훈련데이터와 테스트데이터 나누기 (Cross-validation)


9. 훈련데이터 시각화하기


10. 판다스 데이터로 변환하기 (DB insert를 위해서)

train_target = train_target.reshape(39, 1)
train = np.hstack((train_data, train_target))
train_dataFrame = pd.DataFrame(train, columns=["train_length", "train_weight","train_target"])


11. DB에 insert 하기 - 스킵

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")
train_dataFrame.to_sql("train",engine, index=False,if_exists="replace")
test_dataFrame.to_sql("test",engine, index=False,if_exists="replace")


