import shutil  # Pour obtenir la taille du terminal
import time  # Pour mesurer le temps d'exécution

def ft_tqdm(lst: range) -> None:
    """
    Custom tqdm implementation using a generator to display a progress bar
    with the percentage of completion, the number of iterations, the elapsed time,
    the remaining time and the number of iterations per second.
    """

    length = len(lst)
    terminal_width = shutil.get_terminal_size().columns
    start = time.time()
    update = start

    for i, value in enumerate(lst):
        percent = (i+1) / length * 100
        bar_len = terminal_width - 45
        fill = int(bar_len * (i+1) / length)
        loading_bar = '█' * fill + ' ' * (bar_len - fill)

        # maj du temps écoulé
        update = time.time()
        current_duration = update - start

        # Estimation du temps restant
        if percent != 0:
            remaining = current_duration / (percent / 100) - current_duration
        
        s = int(current_duration % 60)
        m = int(current_duration // 60)
        rs = int(remaining % 60)
        rm = int(remaining // 60)

        itps = 0
        # On évite la division par zéro au debut
        if current_duration > 0.1:
            itps = (i+1) / current_duration  

        # \r -> reecriture de la ligne
        # 02 -> affichage sur 2 chiffres
        # .2f -> affichage sur 2 chiffres après la virgule
        print(f"\r{int(percent):3d}%|{loading_bar}| {i}/{length}\
 [{m:02}:{s:02}<{rm:02}:{rs:02}, {itps:.2f}it/s]", end='')
        # Retourne la valeur actuelle de lst sans interrompre la boucle
        yield value  
