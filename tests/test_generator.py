from qface.generator import FileSystem, Generator
import logging
import logging.config
from pathlib import Path

# logging.config.fileConfig('logging.ini')
logging.basicConfig()

log = logging.getLogger(__name__)

inputPath = Path('tests/in')
log.debug('input path folder: {0}'.format(inputPath.absolute()))


def loadSystem():
    path = inputPath / 'com.pelagicore.ivi.tuner.qdl'
    return FileSystem.parse_document(path)


def test_gen_module():
    system = loadSystem()
    gen = Generator(searchpath='tests/templates')
    template = "{{module}}"
    module = system.lookup('com.pelagicore.ivi.tuner')
    text = gen.apply(template, {"module": module})
    assert text == 'com.pelagicore.ivi.tuner'


def test_gen_interface():
    system = loadSystem()
    gen = Generator(searchpath='tests/templates')
    template = """
        {%- for interface in module.interfaces -%}
            {{interface}}
        {%- endfor -%}
    """
    module = system.lookup('com.pelagicore.ivi.tuner')
    text = gen.apply(template, {"module": module})
    assert text == 'Tuner'


def test_parse_document():
    system = FileSystem.parse(inputPath / 'com.pelagicore.ivi.tuner.qdl')
    assert system.lookup('com.pelagicore.ivi.tuner')


def test_parse_document_list():
    input = [inputPath / 'com.pelagicore.ivi.tuner.qdl', inputPath / 'com.pelagicore.ivi.climate.qdl']
    system = FileSystem.parse(input)
    assert system.lookup('com.pelagicore.ivi.tuner')
    assert system.lookup('com.pelagicore.ivi.climate')


def test_parse_document_mixed():
    input = [inputPath, inputPath / 'com.pelagicore.ivi.climate.qdl']
    system = FileSystem.parse(input)
    assert system.lookup('com.pelagicore.ivi.tuner')
    assert system.lookup('com.pelagicore.ivi.climate')
    assert system.lookup('com.pelagicore.one')
