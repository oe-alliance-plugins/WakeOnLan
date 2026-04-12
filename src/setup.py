from setuptools import setup
import setup_translate

pkg = 'Extensions.WakeOnLan'
setup(name='enigma2-plugin-extensions-wakeonlan',
       version='0.1',
       description='Sends Wake-On-LAN packets when recording etc.',
       package_dir={pkg: 'WakeOnLan'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
