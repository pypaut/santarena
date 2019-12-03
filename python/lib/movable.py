class Movable:
    # Collision
    def collides(self, collidable):
        condH = (
            self.posH < collidable.posH + collidable.rectH
            and self.posH > collidable.posH - self.rectH
        )
        condW = (
            self.posW < collidable.posW + collidable.rectW
            and self.posW > collidable.posW - self.rectW
        )
        return condH and condW

    def reset_contact(self, collidable):
        """
        Compute distances from current position to contact in 4 directions.
        Keep minimal vertical and horizontal distances to deduct collision
        direction.
        """
        # Compute distances from outside
        down_dist = abs(collidable.posH + collidable.rectH - self.posH)
        up_dist = abs(self.posH + self.rectH - collidable.posH)
        left_dist = abs(self.posW + self.rectW - collidable.posW)
        right_dist = abs(collidable.posW + collidable.rectW - self.posW)

        # Collision direction
        gapH = min(down_dist, up_dist)
        gapW = min(right_dist, left_dist)
        if gapW > gapH:  # Vertical move
            self.posH -= self.dirH * min(down_dist, up_dist)
        elif gapH > gapW:  # Horizontal move
            self.posW -= self.dirW * min(right_dist, left_dist)
        else:  # Diagonal move
            self.posH -= self.dirH * min(down_dist, up_dist)
            self.posW -= self.dirW * min(right_dist, left_dist)
