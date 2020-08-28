import xml.etree.ElementTree as et


def get_stats_str(lst):
    result = [str(i) + ':' + str(k) + '\n' for i in list(lst.keys()) for k in list(lst.values())]
    result = list(set(result))
    return ''.join(result)

# collect OS information
def get_os_family(root):
    system_info = root.find("sys")
    if system_info is None:
        return ''
    for info in system_info:
        if info.tag == "os_family":
            return info.text

# collect processor information
def get_processor_description(root):
    proc_info = root.find("processor/item")
    if proc_info is None:
        return ''
    for info in proc_info:
        if info.tag == "description":
            return info.text

# collect memory information
def get_memory_size(root):
    mem_info = root.find("memory")
    if mem_info is None:
        return '0'
    size = 0
    for info in mem_info:
        if info.tag == "size":
            size += int(info.text)
    return str(size)

# collect video card information
def get_video_card_model_and_size(root):
    video_info = root.find("video/item")
    if video_info is None:
        return '', ''
    manufacturer = []
    for info in video_info:
        if info.tag == "manufacturer":
            manufacturer.append(info.text)
    return manufacturer

# get audio card information
def get_audio_card_model(root):
    sound_info = root.find("sound/item")
    if sound_info is None:
        return ''
    for info in sound_info:
        if info.tag == "model":
            return info.text


def parse_data(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    os_family = get_os_family(root)
    proc_description = get_processor_description(root)
    video_card = get_video_card_model_and_size(root)
    audio_card = get_audio_card_model(root)

    return os_family, proc_description, \
           video_card, audio_card


def parse_sys_info(root):
    system_info = root.find("sys")

    if system_info is None:
        return ''

    sys_data = []

    for info in system_info:
        if info.text is not None:
            sys_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(sys_data)

    return result


def parse_processor_info(root):
    processor_info = root.find("processor/item")

    if processor_info is None:
        return ''

    processor_data = []

    for info in processor_info:
        if info.text is not None:
            processor_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(processor_data)

    return result


def parse_memory_info(root):
    memory_info = root.find("memory")

    if memory_info is None:
        return ''

    memory_data = []
    for info in memory_info.findall("item"):
        for item in info:
            print(item.tag, item.text)
            memory_data.append(str(item.tag + ":" + item.text + '\n'))

    result = ''.join(memory_data)

    return result


def parse_motherboard_info(root):
    motherboard_info = root.find("motherboard/item")

    if motherboard_info is None:
        return ''

    motherboard_data = []

    for info in motherboard_info:
        if info.text is not None:
            motherboard_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(motherboard_data)

    return result


def parse_video_card_info(root):
    video_card_info = root.find("video/item")
    if video_card_info is None:
        return ''

    video_card_data = []

    for info in video_card_info:
        if info.text is not None:
            video_card_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(video_card_data)

    return result


def parse_sound_info(root):
    sound_info = root.find("sound/item")

    if sound_info is None:
        return ''

    sound_data = []

    for info in sound_info:
        if info.text is not None:
            sound_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(sound_data)

    return result


def parse_ip_info(root):
    ip_info = root.findall("ip")

    if ip_info is None:
        return ''

    ip_data = []

    for item in ip_info:
        for info in item:
            if info.text is not None:
                ip_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(ip_data)

    return result


def parse_disk_info(root):
    disk_info = root.findall("disk")

    if disk_info is None:
        return ''

    disk_data = []

    for item in disk_info:
        for info in item:
            print(info.tag, info.text, sep=' : ', end='\n')
            if info.text is not None:
                disk_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(disk_data)

    return result


def parse_client_response(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    sys_data = parse_sys_info(root)
    processor_data = parse_processor_info(root)
    memory_data = parse_memory_info(root)
    motherboard_data = parse_motherboard_info(root)
    sound_data = parse_sound_info(root)
    video_card_data = parse_video_card_info(root)
    network_data = parse_ip_info(root)

    return sys_data, processor_data, memory_data, \
           motherboard_data, sound_data, video_card_data, \
           network_data
