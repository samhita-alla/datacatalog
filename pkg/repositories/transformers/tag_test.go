package transformers

import (
	"testing"

	datacatalog "github.com/lyft/flyteidl/gen/pb-go/flyteidl/datacatalog"
	"github.com/stretchr/testify/assert"
)

func TestToTagKey(t *testing.T) {
	datasetID := datacatalog.DatasetID{
		Project: "testProj",
		Domain:  "testDomain",
		Name:    "testName",
		Version: "testVersion",
	}

	tagName := "testTag"
	tagKey := ToTagKey(datasetID, tagName)

	assert.Equal(t, tagName, tagKey.TagName)
	assert.Equal(t, datasetID.Project, tagKey.DatasetProject)
	assert.Equal(t, datasetID.Domain, tagKey.DatasetDomain)
	assert.Equal(t, datasetID.Name, tagKey.DatasetName)
	assert.Equal(t, datasetID.Version, tagKey.DatasetVersion)
}
