# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:09:35 2020

@author: lijing
"""

# import sys
import numpy as np
# import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.models import load_model
# import CNN as CNNmodel
# import cosSimilarity as cos


import os
import importlib, sys

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

importlib.reload(sys)

os.environ['CUDA_VISIBLE_DEVICES'] = '/gpu:0'


def cosine_similarity(x, y):
    num = np.dot(x, y)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    if (x == y).all():
        result = 1.0
    elif denom == 0:
        result = 0.0
    else:
        result = num / denom
    return result


## 随机数
# index = random.randint(0, X_test.shape[0])
# x = X_test[index]
# y = y_test[index]
#
## 显示该数字
# plt.imshow(x, cmap='gray_r')
# plt.title("original {}".format(y))
# plt.show()
def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def text_save01(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'w')
    s = str(data)  # 去除[],这两行按数据不同，可以选择
    file.write(s)
    file.close()
    print("保存wenjian 成功")


def extract(path, labelname):
    # 数据集
    def readExcel(path, labelname):
        #    test_path=r'D:\Echo\毕设\数据及说明\data0401\splitData\001-bg-01-000.xls'
        test_path = path + labelname
        test = pd.read_excel(test_path)
        return test

    def encode(test):
        label_encoder = LabelEncoder().fit(test.classes)
        labels = label_encoder.transform(test.classes)
        classes = list(label_encoder.classes_)
        test = test.drop(['classes', '标签', 'FRAMED'], axis=1)
        return labels, test, classes

    labels, test, classes = encode(readExcel(path, labelname))

    scaler_2 = StandardScaler().fit(test.values)
    scaled_test = scaler_2.transform(test.values)
    nb_features = 16  # 每类特征的特征数
    X_test_r = np.zeros((len(scaled_test), nb_features, 2))
    X_test_r[:, :, 0] = scaled_test[:, :nb_features]
    X_test_r[:, :, 1] = scaled_test[:, nb_features:]

    # 加载
    mymodel = load_model(r'C:\Users\lijing\.spyder-py3\gaitmodel.h5')
    for layer in mymodel.layers:
        layer.trainable = False
    # 取某一层的输出为输出新建为model，采用函数模型
    dense2_layer_model = Model(inputs=mymodel.input, outputs=mymodel.get_layer('dense_2').output)
    # 以这个model的预测值作为输出
    dense2_output = dense2_layer_model.predict(X_test_r)
    #    print(dense2_output.shape)
    #    text_save('D:\Echo\毕设\数据及说明\data0401\\01.txt',dense2_output[0])
    return dense2_output[0]


if __name__ == '__main__':
    filepath = 'D:\Echo\本科\毕设\数据及说明\data0401\splitData\\'
    first = sys.argv[1] + '.xls'
    second = sys.argv[2] + '.xls'
    first_result_path = sys.argv[3]
    second_result_path = sys.argv[4]
    cosresult_path = sys.argv[5]
    result_path = sys.argv[6]
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print(sys.argv[4])
    print(sys.argv[5])
    print(sys.argv[6])
    print(extract(filepath, first))
    text_save(first_result_path, extract(filepath, first))
    print(extract(filepath, second))
    text_save(second_result_path, extract(filepath, second))
    sim = cosine_similarity(extract(filepath, first), extract(filepath, second))
    text_save01(cosresult_path, sim)
    print(sim)
    no = '两个视频中的人不是同一个人。'
    yes = '**两个视频中的人是同一个人。'
    if sim <= 0.035:
        text_save01(result_path, '1')
        print(no)
    else:
        text_save01(result_path, '0')
        print(yes)
# mymodel.summary()
# loss, acc = mymodel.evaluate(X_test_r,classes)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))
# 预测
# x.#mymodel.summary()
# loss, acc = mymodel.evaluate(X_test_r,classes)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))
# 预测
# x.shape = (1,784)#变成[[]]
# x = x.flatten()[None]  # 也可以用这个
# predict = mymodel.predict(X_test_r)
# x = x.flatten()[None]  # 也可以用这个
# predict = mymodel.predict(X_test_r)
# mymodel.summary()
# loss, acc = mymodel.evaluate(X_test_r,classes)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))
# 预测
# x.shape = (1,784)#变成[[]]
# x = x.flatten()[None]  # 也可以用这个
# predict = mymodel.predict(X_test_r)

#
# print('index:', index)
# print('original:', y)
# print('predicted:', predict)

# base_dir = 'data/cnews'
# train_dir = os.path.join(base_dir, 'cnews.train.txt')
# test_dir = os.path.join(base_dir, 'cnews.test.txt')
# val_dir = os.path.join(base_dir, 'cnews.val.txt')
# vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')
#
# save_dir = 'checkpoints/textcnn'
# save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径
#
#
# def get_time_dif(start_time):
#    """获取已使用时间"""
#    end_time = time.time()
#    time_dif = end_time - start_time
#    return timedelta(seconds=int(round(time_dif)))
#
#
# def feed_data(x_batch, y_batch, keep_prob):
#    feed_dict = {
#        model.input_x: x_batch,
#        model.input_y: y_batch,
#        model.keep_prob: keep_prob
#    }
#    return feed_dict
#
#
# def evaluate(sess, x_, y_):
#    """评估在某一数据上的准确率和损失"""
#    data_len = len(x_)
#    batch_eval = batch_iter(x_, y_, 128)
#    total_loss = 0.0
#    total_acc = 0.0
#    for x_batch, y_batch in batch_eval:
#        batch_len = len(x_batch)
#        feed_dict = feed_data(x_batch, y_batch, 1.0)
#        loss, acc = sess.run([model.loss, model.acc], feed_dict=feed_dict)
#        total_loss += loss * batch_len
#        total_acc += acc * batch_len
#
#    return total_loss / data_len, total_acc / data_len
#
#
# def train():
#    print("Configuring TensorBoard and Saver...")
#    # 配置 Tensorboard，重新训练时，请将tensorboard文件夹删除，不然图会覆盖
#    tensorboard_dir = 'tensorboard/textcnn'
#    if not os.path.exists(tensorboard_dir):
#        os.makedirs(tensorboard_dir)
#
#    tf.summary.scalar("loss", model.loss)
#    tf.summary.scalar("accuracy", model.acc)
#    merged_summary = tf.summary.merge_all()
#    writer = tf.summary.FileWriter(tensorboard_dir)
#
#    # 配置 Saver
#    saver = tf.train.Saver()
#    if not os.path.exists(save_dir):
#        os.makedirs(save_dir)
#
#    print("Loading training and validation data...")
#    # 载入训练集与验证集
#    start_time = time.time()
#    x_train, y_train = process_file(train_dir, word_to_id, cat_to_id, config.seq_length)
#    x_val, y_val = process_file(val_dir, word_to_id, cat_to_id, config.seq_length)
#    time_dif = get_time_dif(start_time)
#    print("Time usage:", time_dif)
#
#    # 创建session
#    session = tf.Session()
#    session.run(tf.global_variables_initializer())
#    writer.add_graph(session.graph)
#
#    print('Training and evaluating...')
#    start_time = time.time()
#    total_batch = 0  # 总批次
#    best_acc_val = 0.0  # 最佳验证集准确率
#    last_improved = 0  # 记录上一次提升批次
#    require_improvement = 1000  # 如果超过1000轮未提升，提前结束训练
#
#    flag = False
#    for epoch in range(config.num_epochs):
#        print('Epoch:', epoch + 1)
#        batch_train = batch_iter(x_train, y_train, config.batch_size)
#        for x_batch, y_batch in batch_train:
#            feed_dict = feed_data(x_batch, y_batch, config.dropout_keep_prob)
#
#            if total_batch % config.save_per_batch == 0:
#                # 每多少轮次将训练结果写入tensorboard scalar
#                s = session.run(merged_summary, feed_dict=feed_dict)
#                writer.add_summary(s, total_batch)
#
#            if total_batch % config.print_per_batch == 0:
#                # 每多少轮次输出在训练集和验证集上的性能
#                feed_dict[model.keep_prob] = 1.0
#                loss_train, acc_train = session.run([model.loss, model.acc], feed_dict=feed_dict)
#                loss_val, acc_val = evaluate(session, x_val, y_val)  # todo
#
#                if acc_val > best_acc_val:
#                    # 保存最好结果
#                    best_acc_val = acc_val
#                    last_improved = total_batch
#                    saver.save(sess=session, save_path=save_path)
#                    improved_str = '*'
#                else:
#                    improved_str = ''
#
#                time_dif = get_time_dif(start_time)
#                msg = 'Iter: {0:>6}, Train Loss: {1:>6.2}, Train Acc: {2:>7.2%},' \
#                      + ' Val Loss: {3:>6.2}, Val Acc: {4:>7.2%}, Time: {5} {6}'
#                print(msg.format(total_batch, loss_train, acc_train, loss_val, acc_val, time_dif, improved_str))
#
#            feed_dict[model.keep_prob] = config.dropout_keep_prob
#            session.run(model.optim, feed_dict=feed_dict)  # 运行优化
#            total_batch += 1
#
#            if total_batch - last_improved > require_improvement:
#                # 验证集正确率长期不提升，提前结束训练
#                print("No optimization for a long time, auto-stopping...")
#                flag = True
#                break  # 跳出循环
#        if flag:  # 同上
#            break
#
#
# def test():
#    print("Loading test data...")
#    start_time = time.time()
#    x_test, y_test = process_file(test_dir, word_to_id, cat_to_id, config.seq_length)
#
#    session = tf.Session()
#    session.run(tf.global_variables_initializer())
#    saver = tf.train.Saver()
#    saver.restore(sess=session, save_path=save_path)  # 读取保存的模型
#
#    print('Testing...')
#    loss_test, acc_test = evaluate(session, x_test, y_test)
#    msg = 'Test Loss: {0:>6.2}, Test Acc: {1:>7.2%}'
#    print(msg.format(loss_test, acc_test))
#
#    batch_size = 128
#    data_len = len(x_test)
#    num_batch = int((data_len - 1) / batch_size) + 1
#
#    y_test_cls = np.argmax(y_test, 1)
#    y_pred_cls = np.zeros(shape=len(x_test), dtype=np.int32)  # 保存预测结果
#    for i in range(num_batch):  # 逐批次处理
#        start_id = i * batch_size
#        end_id = min((i + 1) * batch_size, data_len)
#        feed_dict = {
#            model.input_x: x_test[start_id:end_id],
#            model.keep_prob: 1.0
#        }
#        y_pred_cls[start_id:end_id] = session.run(model.y_pred_cls, feed_dict=feed_dict)
#
#    # 评估
#    print("Precision, Recall and F1-Score...")
#    print(metrics.classification_report(y_test_cls, y_pred_cls, target_names=categories))
#
#    # 混淆矩阵
#    print("Confusion Matrix...")
#    cm = metrics.confusion_matrix(y_test_cls, y_pred_cls)
#    print(cm)
#
#    time_dif = get_time_dif(start_time)
#    print("Time usage:", time_dif)
#
#
# if __name__ == '__main__':
#    if len(sys.argv) != 2 or sys.argv[1] not in ['train', 'test']:
#        raise ValueError("""usage: python run_cnn.py [train / test]""")
#
#    print('Configuring CNN model...')
#    config = TCNNConfig()
#    if not os.path.exists(vocab_dir):  # 如果不存在词汇表，重建
#        build_vocab(train_dir, vocab_dir, config.vocab_size)
#    categories, cat_to_id = read_category()
#    words, word_to_id = read_vocab(vocab_dir)
#    config.vocab_size = len(words)
#    model = TextCNN(config)
#
#    if sys.argv[1] == 'train':
#        train()
#    else:
#        test()
