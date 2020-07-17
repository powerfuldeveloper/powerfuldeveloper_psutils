import unittest
from subprocess import DEVNULL

from powerfuldeveloper_psutils.docker.docker_processor import Docker


class TestDocker(unittest.TestCase):

    def setUp(self) -> None:
        self.docker = Docker()

    def test_docker_is_available(self):
        lr: bool
        """ local result"""
        try:
            self.docker.exec('docker')
            lr = True
        except:
            lr = False

        r = self.docker.is_docker_available
        """ result """
        self.assertEqual(lr, r)

    def test_docker_images(self):
        self.assertTrue(self.docker.is_docker_available)
        j = self.docker.images()
        self.assertIsInstance(j, list)

    def test_docker_ps(self):
        self.assertTrue(self.docker.is_docker_available)
        j = self.docker.ps()
        self.assertIsInstance(j, list)


if __name__ == '__main__':
    unittest.main()
