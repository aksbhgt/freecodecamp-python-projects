def hanoi_solver(n):
    rod_a = list(range(n, 0, -1))
    rod_b = []
    rod_c = []

    moves = []

    moves.append(f"{rod_a} {rod_b} {rod_c}")

    def move_disks(number, source, auxiliary, target):
        if number == 1:
            disk = source.pop()
            target.append(disk)

            moves.append(f"{rod_a} {rod_b} {rod_c}")
            return

        move_disks(number - 1, source, target, auxiliary)

        disk = source.pop()
        target.append(disk)

        moves.append(f"{rod_a} {rod_b} {rod_c}")

        move_disks(number - 1, auxiliary, source, target)

    move_disks(n, rod_a, rod_b, rod_c)

    return "\n".join(moves)