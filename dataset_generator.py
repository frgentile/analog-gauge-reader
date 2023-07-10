import cv2
import math


def draw_first_scale(img, center, radius, arc_angles, color):
    # Unpack center coordinates
    xc, yc = center
    # Unpack angles
    start_angle, end_angle = arc_angles

    # cv2.circle(img, (xc, yc), 10, (255, 0, 0), cv2.FILLED, cv2.LINE_AA)

    # Draw scale line
    # # cv2.circle(gauge_background, (xc, yc), r_scale1, scale1_color, 1, cv2.LINE_AA)
    cv2.ellipse(img, (xc, yc), (radius, radius), 0, start_angle, end_angle, color, 1, cv2.LINE_AA)

    # Draw scale's marks
    main_mark_len = 15
    sub_mark_len = 9
    main_marks_qty = 10
    sub_marks_qty = 10
    total_marks_qty = main_marks_qty * sub_marks_qty
    mark_delta_angle = abs(end_angle-start_angle)/total_marks_qty

    # Font Parameters
    font_face = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1.0
    font_thickness = 2

    draw_main = True
    sub_count = 0
    for i in range(0, total_marks_qty+1):
        if draw_main:
            # Calculate coordinates
            start_point = (xc + int(radius * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                           yc + int(radius * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            end_point = (xc + int((radius + main_mark_len) * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                         yc + int((radius + main_mark_len) * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            cv2.line(img, start_point, end_point, color, 3, cv2.LINE_AA)

            # Put Text
            # 1. Get text dim
            text_size, _ = cv2.getTextSize(f"{i}", font_face, font_scale, font_thickness)
            tw, th = text_size
            # 2. Calculate bottom-left coordinate
            tx = xc + int((radius + 30) * math.cos(math.radians(start_angle + i * mark_delta_angle))) - int(tw/2)
            ty = yc + int((radius + 30) * math.sin(math.radians(start_angle + i * mark_delta_angle))) + int(th/2)
            start_point = (tx, ty)
            # 3. Draw text
            cv2.putText(img, f"{i}", start_point, font_face, font_scale, color, font_thickness, cv2.LINE_AA)

            draw_main = False
            sub_count = 0
        else:
            delta_radius = 0
            if sub_count == (sub_marks_qty // 2)-1:
                delta_radius = 5
            # Calculate coordinates
            start_point = (xc + int(radius * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                           yc + int(radius * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            end_point = (xc + int((radius + sub_mark_len + delta_radius) * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                         yc + int((radius + sub_mark_len + delta_radius) * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            cv2.line(img, start_point, end_point, color, 1, cv2.LINE_AA)
            sub_count += 1
            if sub_count == sub_marks_qty-1:
                draw_main = True


def draw_second_scale(img, center, radius, arc_angles, color):
    # Unpack center coordinates
    xc, yc = center
    # Unpack angles
    start_angle, end_angle = arc_angles

    # cv2.circle(img, (xc, yc), 10, (255, 0, 0), cv2.FILLED, cv2.LINE_AA)

    # Draw scale line
    # # cv2.circle(gauge_background, (xc, yc), r_scale1, scale1_color, 1, cv2.LINE_AA)
    cv2.ellipse(img, (xc, yc), (radius, radius), 0, start_angle, end_angle, color, 1, cv2.LINE_AA)

    # Draw scale's marks
    main_mark_len = 15
    sub_mark_len = 9
    main_marks_qty = 7
    sub_marks_qty = 10
    total_marks_qty = main_marks_qty * sub_marks_qty
    mark_delta_angle = abs(end_angle-start_angle)/total_marks_qty

    # Font Parameters
    font_face = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1.0
    font_thickness = 2

    draw_main = True
    sub_count = 0
    for i in range(0, total_marks_qty+1):
        if draw_main:
            # Calculate coordinates
            start_point = (xc + int(radius * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                           yc + int(radius * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            end_point = (xc + int((radius - main_mark_len) * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                         yc + int((radius - main_mark_len) * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            cv2.line(img, start_point, end_point, color, 3, cv2.LINE_AA)

            # Put Text
            # 1. Get text dim
            text_size, _ = cv2.getTextSize(f"{i//10}", font_face, font_scale, font_thickness)
            tw, th = text_size
            # 2. Calculate bottom-left coordinate
            tx = xc + int((radius - 30) * math.cos(math.radians(start_angle + i * mark_delta_angle))) - int(tw/2)
            ty = yc + int((radius - 30) * math.sin(math.radians(start_angle + i * mark_delta_angle))) + int(th/2)
            start_point = (tx, ty)
            # 3. Draw text
            cv2.putText(img, f"{i//10}", start_point, font_face, font_scale, color, font_thickness, cv2.LINE_AA)

            draw_main = False
            sub_count = 0
        else:
            delta_radius = 0
            if sub_count == (sub_marks_qty // 2)-1:
                delta_radius = 5
            # Calculate coordinates
            start_point = (xc + int(radius * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                           yc + int(radius * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            end_point = (xc + int((radius - sub_mark_len - delta_radius) * math.cos(math.radians(start_angle + i * mark_delta_angle))),
                         yc + int((radius - sub_mark_len - delta_radius) * math.sin(math.radians(start_angle + i * mark_delta_angle))))
            cv2.line(img, start_point, end_point, color, 1, cv2.LINE_AA)
            sub_count += 1
            if sub_count == sub_marks_qty-1:
                draw_main = True


def main():
    # Load background image
    gauge_background = cv2.imread('images/pressure-gauge.png')
    # Get Shape of gauge_background (gb)
    gb_h, gb_w, gb_c = gauge_background.shape
    print(f"Background Image Size: {gauge_background.shape}")

    # Coordinates of the center
    xc, yc = 253, 202

    # # Radius of the center point
    # rc_min = 10
    # Greater Radius
    # rc_max = 150
    rc_max = 160
    # First Scale Radius
    r_scale1 = 113
    # Second Scale Radius
    r_scale2 = 107

    # Background color for the generated gauge
    background_color = (209, 207, 206)
    # background_color = (239, 237, 236)
    # First Scale color
    scale1_color = (0, 0, 124)
    # Second Scale color
    scale2_color = (0, 0, 0)

    # Draw the circle to prepare the "canvas"
    cv2.circle(gauge_background, (xc, yc), rc_max, background_color, cv2.FILLED, cv2.LINE_AA)

    # First Scale Drawing
    draw_first_scale(gauge_background, (xc, yc), r_scale1, (137, 407), scale1_color)
    # Second Scale Drawing
    draw_second_scale(gauge_background, (xc, yc), r_scale2, (137, 407), scale2_color)

    # cv2.circle(gauge_background, (xc, yc), (r_scale1, r_scale1), 0, 138, 407, (255, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow("Preview", gauge_background)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
