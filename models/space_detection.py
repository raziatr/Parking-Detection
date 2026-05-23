import pickle
import cv2

with open("ParkPos", "rb") as f:
    pos_list = pickle.load(f)

slot_history = {}
THRESHOLD = 870

width, height = 80, 30

def check_space(image_pro, img):

    space_counter = 0

    for i, pos in enumerate(pos_list):

        x, y = pos

        img_crop = image_pro[y:y + height, x:x + width]

        count = cv2.countNonZero(img_crop)

        # simpan history
        slot_history[i].append(count)

        # ambil 20 frame terakhir
        if len(slot_history[i]) > 20:
            slot_history[i].pop(0)

        # average
        avg_count = sum(slot_history[i]) / len(slot_history[i])

        # decision berdasarkan average
        if avg_count < THRESHOLD:
            color = (0, 255, 0)
            thickness = 5
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(
            img,
            pos,
            (pos[0] + width, pos[1] + height),
            color,
            thickness
        )

        cv2.putText(
            img,
            str(int(avg_count)),
            (x, y + height - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255),
            1
        )

    cv2.putText(
        img,
        f"Free: {space_counter}/{len(pos_list)}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )
