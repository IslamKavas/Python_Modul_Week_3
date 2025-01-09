def add_task(task_list, task_sequence):
    """
    Yeni bir görev ekler.
    """
    task_sequence += 1
    task_name = input("Lütfen görev için bir isim girin: ")
    task_list[task_sequence] = {'name': task_name, 'status': 'Tamamlanmadı'}
    print(f"\nYeni görev '{task_name}' {task_sequence} ID ile listeye eklendi.\n")
    return task_sequence

def complete_task(task_list):
    """
    Bir görevi tamamlanmış olarak işaretler.
    """
    try:
        task_id = int(input("Lütfen görev ID'sini girin: "))
        if task_id in task_list:
            task_list[task_id]['status'] = 'Tamamlandı'
            print(f"\nGörev {task_id} tamamlandı.\n")
        else:
            print("\nGörev ID bulunamadı.\n")
    except ValueError:
        print("\nGeçersiz giriş. Lütfen bir sayı girin.\n")

def delete_task(task_list):
    """
    Bir görevi siler.
    """
    try:
        task_id = int(input("Lütfen silinecek görev ID'sini girin: "))
        if task_id in task_list:
            del task_list[task_id]
            print(f"Görev {task_id} silindi.\n")
        else:
            print("\nGörev ID bulunamadı.\n")
    except ValueError:
        print("\nGeçersiz giriş. Lütfen bir sayı girin.\n")

def list_completed_tasks(task_list):
    """
    Tamamlanmış görevleri listeler.
    """
    print("Tamamlanmış Görevler:")
    completed = False
    for task_id, task in task_list.items():
        if task['status'] == 'Tamamlandı':
            print(f"ID: {task_id}, İsim: {task['name']}")
            completed = True
    if not completed:
        print("Tamamlanmış görev bulunamadı.\n")

def list_all_tasks(task_list):
    """
    Tüm görevleri durumlarıyla birlikte listeler.
    """
    print("Tüm Görevler ve Durumları:")
    if not task_list:
        print("Görev listesi boş.\n")
    else:
        for task_id, task in task_list.items():
            print(f"ID: {task_id}, İsim: {task['name']}, Durum: {task['status']}")
        print("Görevlerin durumları listelendi.\n")

def main():
    task_list = {}
    task_sequence = 100

    while True:
        print("Görev Yönetim Sistemi\n")
        print("Lütfen aşağıdaki işlemlerden birini seçin.\n")
        print("1. Yeni bir görev ekle")
        print("2. Bir görevi tamamla")
        print("3. Bir görevi sil")
        print("4. Tamamlanmış görevleri listele")
        print("5. Tüm görevleri durumlarıyla listele")
        print("6. Çıkış\n")

        choice = input("Yapmak istediğiniz işlem numarasını girin: ")

        if choice == '1':
            task_sequence = add_task(task_list, task_sequence)
        elif choice == '2':
            complete_task(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            list_completed_tasks(task_list)
        elif choice == '5':
            list_all_tasks(task_list)
        elif choice == '6':
            print("Görev yönetim sisteminden çıkılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin!")


def add_task(task_list, task_sequence):
    """
    Yeni bir görev ekler.
    """
    task_sequence += 1
    task_name = input("Lütfen görev için bir isim girin: ")
    task_list[task_sequence] = {'name': task_name, 'status': 'Tamamlanmadı'}
    print(f"\nYeni görev '{task_name}' {task_sequence} ID ile listeye eklendi.\n")
    return task_sequence

def complete_task(task_list):
    """
    Bir görevi tamamlanmış olarak işaretler.
    """
    try:
        task_id = int(input("Lütfen görev ID'sini girin: "))
        if task_id in task_list:
            task_list[task_id]['status'] = 'Tamamlandı'
            print(f"\nGörev {task_id} tamamlandı.\n")
        else:
            print("\nGörev ID bulunamadı.\n")
    except ValueError:
        print("\nGeçersiz giriş. Lütfen bir sayı girin.\n")

def delete_task(task_list):
    """
    Bir görevi siler.
    """
    try:
        task_id = int(input("Lütfen silinecek görev ID'sini girin: "))
        if task_id in task_list:
            del task_list[task_id]
            print(f"Görev {task_id} silindi.\n")
        else:
            print("\nGörev ID bulunamadı.\n")
    except ValueError:
        print("\nGeçersiz giriş. Lütfen bir sayı girin.\n")

def list_completed_tasks(task_list):
    """
    Tamamlanmış görevleri listeler.
    """
    print("Tamamlanmış Görevler:")
    completed = False
    for task_id, task in task_list.items():
        if task['status'] == 'Tamamlandı':
            print(f"ID: {task_id}, İsim: {task['name']}")
            completed = True
    if not completed:
        print("Tamamlanmış görev bulunamadı.\n")

def list_all_tasks(task_list):
    """
    Tüm görevleri durumlarıyla birlikte listeler.
    """
    print("Tüm Görevler ve Durumları:")
    if not task_list:
        print("Görev listesi boş.\n")
    else:
        for task_id, task in task_list.items():
            print(f"ID: {task_id}, İsim: {task['name']}, Durum: {task['status']}")
        print("Görevlerin durumları listelendi.\n")

def main():
    task_list = {}
    task_sequence = 100

    while True:
        print("Görev Yönetim Sistemi\n")
        print("Lütfen aşağıdaki işlemlerden birini seçin.\n")
        print("1. Yeni bir görev ekle")
        print("2. Bir görevi tamamla")
        print("3. Bir görevi sil")
        print("4. Tamamlanmış görevleri listele")
        print("5. Tüm görevleri durumlarıyla listele")
        print("6. Çıkış\n")

        choice = input("Yapmak istediğiniz işlem numarasını girin: ")

        if choice == '1':
            task_sequence = add_task(task_list, task_sequence)
        elif choice == '2':
            complete_task(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            list_completed_tasks(task_list)
        elif choice == '5':
            list_all_tasks(task_list)
        elif choice == '6':
            print("Görev yönetim sisteminden çıkılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin!")

if __name__ == "__main__":
    main()


